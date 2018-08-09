from bs4 import Tag, NavigableString


def pivot_pandas_to_excel(soup, show_intermediate_breakdown=False, show_total_breakdown=False):
    '''pandas style pivot to excel style pivot formatting for outlook/html

    This function is meant to be provided to the email functionality as a postprocessor.
    It expects a jupyter or pandas exported html table of a dataframe with the following index:

    example:
    # a single pivot
    pt1 = pd.pivot_table(data,
                         value=['col1', 'col2', 'col3'],
                         index=['index'],
                         columns=['col4'],
                         aggfunc='sum',
                         margins=True).stack('col4')

    # here we reindex the table to have the appropriate row ordering
    pt1 = pt1.reindex(
            pd.MultiIndex(
            levels=[['COL1', 'COL2', 'All'],
                    ['ROW1', 'ROW2', 'ALL']],
            labels=[[0, 0, 0, 1, 1, 1, 2], # This is the key, changing the label order (2-ALL)
                    [2, 0, 1, 2, 0, 1, 2]],
            names=['', ''],
            sortorder=0)
            ).fillna(0)

    show_intermediate_breakdown --> intermediate sumations to be shown?
    show_total_breakdown --> total sumations to be shown?
    '''
    tables = soup.findAll('table')
    for table in tables:

        # delete second row (empty in pivot table)
        table.thead.findChildren('tr')[1].decompose()
        new_body = Tag(name='tbody')
        bc = 0

        # max number of columns so table is even
        num_columns_max = max(len(row.findAll()) for row in table.tbody.findAll('tr'))
        num_headers_max = max(len(row.findAll('th')) for row in table.tbody.findAll('tr'))

        # for special case where we delete the summation rows
        last = False

        # construct new rows from pivot headers
        for row in table.tbody.findChildren('tr'):
            headers = list(row.findChildren('th'))
            data = list(row.findChildren('th'))

            # if multiple headers, reduce into new rows
            if len(headers) > 1:
                # omit if total breakdown deactivated
                if 'All' in headers[0].contents:
                    last = True

                # control indentation to match pivot levels
                indent = 0

                # first header has special formatting
                first_header = (len(headers) == num_headers_max)

                # reduce into more rows if not skipping
                if not last:
                    for header in headers[:-1]:
                        # one header per row, blank data
                        new_row = Tag(name='tr', attrs={'class': 'empty_pivot_row_first'}) if first_header else Tag(name='tr', attrs={'class': 'empty_pivot_row'})

                        # omit empty rows
                        if not header.contents:
                            # empty header means spans multiple columns, omit
                            continue

                        # new header to delete formatting
                        new_header = Tag(name='th', attrs={'class': 'empty_pivot_row_first',
                                                           'style': 'margin-left:' + str(10*(num_headers_max - len(headers) + indent)) + 'px;'}) if first_header else \
                            Tag(name='th', attrs={'class': 'empty_pivot_row',
                                                  'style': 'margin-left:' + str(10*(num_headers_max - len(headers) + indent)) + 'px;'})

                        new_header.contents = header.contents
                        new_row.insert(0, new_header)

                        # fill in blanks for data
                        for j in range(num_columns_max-1):
                            new_row.insert(j+1, Tag(name='td', attrs={'class': 'empty_pivot_row_first'})) if first_header else new_row.insert(j+1, Tag(name='td', attrs={'class': 'empty_pivot_row'}))

                        new_body.insert(bc, new_row)

                        bc += 1
                        indent += 1
                        first_header = False

            # then insert the data with no headers
            new_row = Tag(name='tr')

            # increase pivot indent
            new_header = Tag(name='th', attrs={'class': 'pivot_row_header',
                                               'style': 'margin-left:' + str(10*(num_headers_max-1)) + 'px;'})
            new_header.contents = headers[-1].contents

            # change sum total
            if 'All' in headers[-1].contents:
                if not show_intermediate_breakdown and not last:
                    continue
                elif not show_intermediate_breakdown:
                    last = False
                    new_row = Tag(name='tr', attrs={'class': 'total_pivot_row'})
                    new_header = Tag(name='th', attrs={'class': 'total_pivot_row'})
                    new_header.contents = [NavigableString('Grand Total')]
                elif not last:
                    pass

            # omit intermediate rows if skipping
            if last:
                continue

            # insert header into new row
            new_row.insert(0, new_header)

            # fill in blank headers
            cc = 1
            for _ in range(num_columns_max - len(data) - 1):
                new_header = Tag(name='th', attrs={'class': 'total_pivot_row'}) if 'All' in headers[-1].contents else Tag(name='th')
                new_row.insert(cc, new_header)
                cc += 1

            # copy data into row
            for dat in data:
                new_data = Tag(name='td') if 'All' not in headers[-1].contents else Tag(name='td', attrs={'class': 'total_pivot_row'})
                new_data.contents = dat.contents
                new_row.insert(cc, new_data)
                cc += 1

            # insert row into new body
            new_body.insert(bc, new_row)

            # increment count but not indent
            bc += 1

        # swap out the old body with the newly constructed one
        table.tbody.replaceWith(new_body)
    return soup
