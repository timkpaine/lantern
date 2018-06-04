{%- extends 'display_priority.tpl' -%}

{% block header %}
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <title>Report</title>
<style type="text/css">
    body {
        font-family: Calibri;
        text-align: justify;
        line-height: 1.1;
        font-weight: normal;
        letter-spacing: normal;
    }

    div {

    }

    img {
        width: 640px !important;
        white-space: nowrap;
        padding: 0px;
        margin-left: 20px;
        margin-top: 0px;
    }

    h1 {
        background-color: #7397bc;
        color:white;
        height: 50px !important;
        padding:0px;
        margin-top:20px;
        margin-bottom: 10px;
    }

    h2 {
        border-bottom: 4px solid #7397bc;
        color: #444;
        padding: 0px;
        margin-top: 20px;
        margin-bottom: 10px;
    }

    h3 {
        color:#222;
        padding:0px;
        margin-top: 20px;
        margin-bottom: 10px;
    }

    td {
        text-align:right;
        padding:2px;
        margin-top:2px;
    }

    th {
        font-weight: normal;
        text-align: left;
        margin-top: 2px;
    }

    thead {
        background-color: #dce6f1;
        padding: 2px;
    }

    thead th {
        font-weight: bold;
        text-align: center;
        padding-left: 10px;
        padding-bottom: 2px;
        border-bottom: 1px solid #95b3d7;
    }

    tr {
        border-bottom: 1px solid #DDD;
    }

    th.pivot_row_header{}
    tr.empty_pivot_row{}
    tr.empty_pivot_row_first{}

    th.empty_pivot_row{
        font-weight: bold;
        padding-left:2px;
    }

    th.empty_pivot_row_first{
        font-weight: bold;
        border-bottom: 1px solid #95b3d7;
        padding-left: 2px;
    }

    td.empty_pivot_row{}

    td.empty_pivot_row_first{
        border-bottom: 1px solid #95b3d7;
    }

    tr.total_pivot_row {
        background-color: #dce6f1;
    }

    th.total_pivot_row {
        font-weight: bold;
        padding-left: 2px;
        border-top: 1px solid #95b3d7;
    }

    td.total_pivot_row {
        border-top: 1px solid #95b3d7;
        font-weight: bold;
    }

    table {
        margin-top: 10px;
        margin-left: 10px;
        padding-bottom: 20px;
        padding:0px;
        white-space: nowrap;
        border-collapse: collapse;
        font-family: Calibri, Arial;
        font-size: 9px;
        letter-spacing: normal;
        mso-displayed-decimal-separator: "\.";
        mso-displayed-thousand-separator: "\,";
        table-layout: auto;
        width:600px;
    }

    .header {
        font-size: 0.75em;
    }

    .footer {
        font-size: 0.75em;
    }
</style>
</head>

{{ super() }}
{% endblock header %}
{% block body %}
<body>
<div class="header"></div>
{{ super() }}
<div class="footer"></div>
</body>
{% endblock body %}

{% block codecell %}
<div class="cell border-box-sizing code_cell rendered">
{{ super() }}
</div>
{%- endblock codecell %}

{% block input_group -%}
{% endblock input_group %}

{% block output_group %}
<div class="output_wrapper">
<div class="output">
{{ super() }}
</div>
</div>
{% endblock output_group %}

{% block in_prompt -%}
{%- endblock in_prompt %}

{% block empty_in_prompt -%}
{%- endblock empty_in_prompt %}

{% block output_prompt %}
{% endblock output_prompt %}

{% block input %}
{%- endblock input %}


{% block output_area_prompt %}
{% endblock output_area_prompt %}

{% block output %}
<div class="output_area">
{% if resources.global_content_filter.include_output_prompt %}
{{ self.output_area_prompt() }}
{% endif %}
{{ super() }}
</div>
{% endblock output %}

{% block markdowncell scoped %}
<div class="cell border-box-sizing text_cell rendered">
{%- if resources.global_content_filter.include_input_prompt-%}
    {{ self.empty_in_prompt() }}
{%- endif -%}
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
{{ cell.source  | markdown2html | strip_files_prefix }}
</div>
</div>
</div>
{%- endblock markdowncell %}


{% block unknowncell scoped %}
unknown type  {{ cell.type }}
{% endblock unknowncell %}

{% block execute_result -%}
{%- set extra_class="output_execute_result" -%}
{% block data_priority scoped %}
{{ super() }}
{% endblock data_priority %}
{%- set extra_class="" -%}
{%- endblock execute_result %}

{% block stream_stdout -%}
<div class="output_subarea output_stream output_stdout output_text">
<pre>
{{- output.text | ansi2html -}}
</pre>
</div>
{%- endblock stream_stdout %}

{% block stream_stderr -%}
<div class="output_subarea output_stream output_stderr output_text">
<pre>
{{- output.text | ansi2html -}}
</pre>
</div>
{%- endblock stream_stderr %}


{% block data_svg scoped -%}
<div class="output_svg output_subarea {{ extra_class }}">
{%- if output.svg_filename %}
<img src="{{ output.svg_filename | posix_path }}"
{%- else %}
{{ output.data['image/svg+xml'] }}
{%- endif %}
</div>
{%- endblock data_svg %}



{% block data_html scoped -%}
<div class="output_html rendered_html output_subarea {{ extra_class }}">
{{ output.data['text/html'] }}
</div>
{%- endblock data_html %}


{% block data_markdown scoped -%}
<div class="output_markdown rendered_html output_subarea {{ extra_class }}">
{{ output.data['text/markdown'] | markdown2html }}
</div>
{%- endblock data_markdown %}

{% block data_png scoped %}
<div class="output_png output_subarea {{extra_class}}">
{%- if 'image/png' in output.metadata.get('filenames', {}) %}
<img src="{{output.metadata.filenames['image/png'] | posix_path }}"
{% else %}
<style>
img#{{cell.execution_count}}{
    background:url(data:image/png;base64,{{ output.data['image/png']}}) no-repeat left center;
}
</style>
<img src="cid:{{ cell.execution_count }}" id="{{cell.execution_count}}" cell_id="{{ cell.execution_count }}"  alt="{{cell.execution_count}}" localdata="{{ output.data['image/png'] }}"
{% endif %}
{%- set width=output | get_metadata('width', 'image/png') -%}
{%- if width is not none %}
width={{ width }}
{%- endif %}
{%- set height=output | get_metadata('height', 'image/png') -%}
{%- if height is not none %}
height={{ height }}
{%- endif %}
{%- if output | get_metadata('unconfined', 'image/png') %}
class="unconfined"
{%- endif %}
>
</div>
{%- endblock data_png %}

{% block data_jpg scoped %}
<div class="output_jpeg output_subarea {{ extra_class }}">
{%- if 'image/jpeg' in output.metadata.get('filenames', {}) %}
<img src="{{ output.metadata.filenames['image/jpeg'] | posix_path }}"
{%- else %}
<img src="data:image/jpeg;base64,{{ output.data['image/jpeg'] }}"
{%- endif %}
{%- set width=output | get_metadata('width', 'image/jpeg') -%}
{%- if width is not none %}
width={{ width }}
{%- endif %}
{%- set height=output | get_metadata('height', 'image/jpeg') -%}
{%- if height is not none %}
height={{ height }}
{%- endif %}
{%- if output | get_metadata('unconfined', 'image/jpeg') %}
class="unconfined"
{%- endif %}
>
</div>
{%- endblock data_jpg %}

{% block data_latex scoped %}
<div class="output_latex output_subarea {{ extra_class }}">
{{ output.data['text/latex'] }}
</div>
{%- endblock data_latex %}

{% block error -%}
{%- endblock error %}


{%- block traceback_line %}
{{ line | ansi2html }}
{%- endblock traceback_line %}

{%- block data_text scoped %}
<div class="output_text output_subarea {{ extra_class }}">
<pre>
{{- output.data['text/plain'] | ansi2html -}}
</pre>
</div>
{%- endblock -%}

{%- block data_javascript scoped %}
{% set div_id = uuid4() %}
<div id="{{ div_id }}"></div>
<div class="output_subarea output_javascript {{ extra_class }}">
<script type="text/javascript">
var element = $('#{{ div_id }}');
{{ output.data['application/javascript'] }}
</script>
</div>
{%- endblock -%}

{%- block data_widget_state scoped %}
{% set div_id = uuid4() %}
{% set datatype_list = output.data | filter_data_type %} 
{% set datatype = datatype_list[0]%} 
<div id="{{ div_id }}"></div>
<div class="output_subarea output_widget_state {{ extra_class }}">
<script type="text/javascript">
var element = $('#{{ div_id }}');
</script>
<script type="{{ datatype }}">
{{ output.data[datatype] | json_dumps }}
</script>
</div>
{%- endblock data_widget_state -%}


{%- block data_widget_view scoped %}
{% set div_id = uuid4() %}
{% set datatype_list = output.data | filter_data_type %} 
{% set datatype = datatype_list[0]%} 
<div id="{{ div_id }}"></div>
<div class="output_subarea output_widget_view {{ extra_class }}">
<script type="text/javascript">
var element = $('#{{ div_id }}');
</script>
<script type="{{ datatype }}">
{{ output.data[datatype] | json_dumps }}
</script>
</div>
{%- endblock data_widget_view -%}

{%- block footer %}
{% set mimetype = 'application/vnd.jupyter.widget-state+json'%} 
{% if mimetype in nb.metadata.get("widgets",{})%}
<script type="{{ mimetype }}">
{{ nb.metadata.widgets[mimetype] | json_dumps }}
</script>
{% endif %}
{{ super() }}
{%- endblock footer -%}
</html>


