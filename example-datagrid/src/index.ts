/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
import 'es6-promise/auto';  // polyfill Promise on IE

import {
  DataGrid, JSONModel
} from '@phosphor/datagrid';

import {
  Widget
  // DockPanel, StackedPanel, Widget
} from '@phosphor/widgets';

import '../style/index.css';


// function createWrapper(content: Widget, title: string): Widget {
//   let wrapper = new StackedPanel();
//   wrapper.addClass('content-wrapper');
//   wrapper.addWidget(content);
//   wrapper.title.label = title;
//   return wrapper;
// }


function main(): void {

  // let model5 = new JSONModel(Data.cars);

  let blueStripeStyle: DataGrid.IStyle = {
    ...DataGrid.defaultStyle,
    rowBackgroundColor: i => i % 2 === 0 ? 'rgba(138, 172, 200, 0.3)' : '',
    columnBackgroundColor: i => i % 2 === 0 ? 'rgba(100, 100, 100, 0.1)' : ''
  };


  // let grid5 = new DataGrid({
  //   style: blueStripeStyle,
  //   baseRowSize: 32,
  //   baseColumnSize: 128,
  //   baseRowHeaderSize: 64,
  //   baseColumnHeaderSize: 32
  // });
  // grid5.model = model5;

  // let wrapper5 = createWrapper(grid5, 'JSON Data');

  // let dock = new DockPanel();
  // dock.id = 'dock';

  // dock.addWidget(wrapper5, );

  // window.onresize = () => { dock.update(); };

  // Widget.attach(dock, document.body);

  var submit = <HTMLInputElement>document.getElementById("foo");
  submit.onsubmit = () => {
    var json = submit.value;
    alert(json);
    // model5 = new JSONModel(JSON.parse(json));
    // grid5.model = model5;

    let gridtmp = new DataGrid({
      style: blueStripeStyle,
      baseRowSize: 32,
      baseColumnSize: 128,
      baseRowHeaderSize: 64,
      baseColumnHeaderSize: 32
    });
    let modeltmp = new JSONModel(JSON.parse(json));
    gridtmp.model = modeltmp;
    var elem = document.createElement('div');
    document.body.appendChild(elem);
    Widget.attach(gridtmp, elem);
  };

}


window.onload = main;


// namespace Data {

//   export
//   const cars = {
//     "data": [],
//     "schema": {
//       "primaryKey": [],
//       "fields": [],
//       "pandas_version": "0.20.0"
//     }
//   }
//   //   "data": [
//   //     {
//   //       "Name": "chevrolet chevelle malibu",
//   //       "index": 0,
//   //       "Acceleration": 12.0,
//   //     },
//   //     {
//   //       "Name": "buick skylark 320",
//   //       "index": 1,
//   //       "Acceleration": 11.5,
//   //     },
//   //     {
//   //       "Name": "plymouth satellite",
//   //       "index": 2,
//   //       "Acceleration": 11.0,
//   //     }
//   //   ],
//   //   "schema": {
//   //     "primaryKey": [
//   //       "index"
//   //     ],
//   //     "fields": [
//   //       {
//   //         "name": "index",
//   //         "type": "integer"
//   //       },
//   //       {
//   //         "name": "Acceleration",
//   //         "type": "number"
//   //       },
//   //       {
//   //         "name": "Name",
//   //         "type": "string"
//   //       }
//   //     ],
//   //     "pandas_version": "0.20.0"
//   //   }
//   // }

// }
