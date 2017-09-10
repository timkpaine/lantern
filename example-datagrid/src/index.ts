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

export
function createGrid(json:string, elem: HTMLElement): void {
  let blueStripeStyle: DataGrid.IStyle = {
    ...DataGrid.defaultStyle,
    rowBackgroundColor: i => i % 2 === 0 ? 'rgba(138, 172, 200, 0.3)' : '',
    columnBackgroundColor: i => i % 2 === 0 ? 'rgba(100, 100, 100, 0.1)' : ''
  };

  let gridtmp = new DataGrid({
    style: blueStripeStyle,
    baseRowSize: 32,
    baseColumnSize: 128,
    baseRowHeaderSize: 64,
    baseColumnHeaderSize: 32
  });
  let modeltmp = new JSONModel(JSON.parse(json));
  gridtmp.model = modeltmp;
  Widget.attach(gridtmp, elem);
};

function main(): void {
  let blueStripeStyle: DataGrid.IStyle = {
    ...DataGrid.defaultStyle,
    rowBackgroundColor: i => i % 2 === 0 ? 'rgba(138, 172, 200, 0.3)' : '',
    columnBackgroundColor: i => i % 2 === 0 ? 'rgba(100, 100, 100, 0.1)' : ''
  };
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

export default createGrid