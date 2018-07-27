import {
  JupyterLab, JupyterLabPlugin, ILayoutRestorer
} from '@jupyterlab/application';

import {
  INotebookTracker, NotebookPanel
} from '@jupyterlab/notebook';

import {
  ReadonlyJSONObject
} from '@phosphor/coreutils';

import {
  Menu
} from '@phosphor/widgets';

import {
  URLExt
} from '@jupyterlab/coreutils';

import {
  ICommandPalette
} from '@jupyterlab/apputils';

import {
  IMainMenu
} from '@jupyterlab/mainmenu';


import '../style/index.css';

const extension: JupyterLabPlugin<void> = {
  id: 'jupyterlab_lantern',
  autoStart: true,
  requires: [IMainMenu, ICommandPalette, ILayoutRestorer, INotebookTracker],
  activate: activate
};

function activate(app: JupyterLab,  mainMenu: IMainMenu, palette: ICommandPalette, restorer: ILayoutRestorer, tracker: INotebookTracker) {
  console.log('JupyterLab extension lantern is activated!');

  const { commands, shell } = app;

  function hasWidget(): boolean {
    return tracker.currentWidget !== null;
  }
  function getCurrent(args: ReadonlyJSONObject): NotebookPanel | null {
    const widget = tracker.currentWidget;
    const activate = args['activate'] !== false;

    if (activate && widget) {
      shell.activateById(widget.id);
    }

    return widget;
  }

  let services = app.serviceManager;

  // Add an application command
  const export_pdf = 'lantern:export-pdf';
  const export_html = 'lantern:export-html';
  const publish = 'lantern:publish';

  // const export_html = 'lantern:export-html';
  commands.addCommand(export_pdf, {
    label: 'PDF - no code',
    execute: args => {
      const current = getCurrent(args);

      if (!current) {
        return;
      }

      const notebookPath = URLExt.encodeParts(current.context.path);
      const url = URLExt.join(
        services.serverSettings.baseUrl,
        'nbconvert',
        'pdf_hidecode',
        notebookPath
      ) + '?download=true';
      const child = window.open('', '_blank');
      const { context } = current;

      if (context.model.dirty && !context.model.readOnly) {
        return context.save().then(() => { child.location.assign(url); });
      }

      return new Promise<void>((resolve) => {
        child.location.assign(url);
        resolve(undefined);
      });
    },
    isEnabled: hasWidget
  });

  commands.addCommand(export_html, {
    label: 'HTML - no code',
    execute: args => {
      const current = getCurrent(args);

      if (!current) {
        return;
      }

      const notebookPath = URLExt.encodeParts(current.context.path);
      const url = URLExt.join(
        services.serverSettings.baseUrl,
        'nbconvert',
        'html_hidecode',
        notebookPath
      ) + '?download=true';
      const child = window.open('', '_blank');
      const { context } = current;

      if (context.model.dirty && !context.model.readOnly) {
        return context.save().then(() => { child.location.assign(url); });
      }

      return new Promise<void>((resolve) => {
        child.location.assign(url);
        resolve(undefined);
      });
    },
    isEnabled: hasWidget
  });

  commands.addCommand(publish, {
    label: 'Publish - no code',
    execute: args => {
      const current = getCurrent(args);

      if (!current) {
        return;
      }

      const notebookPath = URLExt.encodeParts(current.context.path);
      const url = URLExt.join(
        services.serverSettings.baseUrl,
        'publish',
        notebookPath
      );
      const { context } = current;


      let request = new XMLHttpRequest();
      request.onreadystatechange = () => {
          if (request.readyState === 4){
            const child = window.open('', '_blank');

            if (context.model.dirty && !context.model.readOnly) {
              return context.save().then(() => { child.location.assign(url); });
            }

            child.location.assign(url);
          }
      };
      request.open('POST', url, true);
      request.setRequestHeader('X-Requested-With', 'XMLHttpRequest');

      let outputs = current.content.node.querySelectorAll('.jp-OutputArea-output, .jp-RenderedMarkdown');
      let to_send = '';
      for(let i = 0; i<outputs.length; i++){
        to_send += outputs[i].outerHTML;
      }
      request.send(to_send);
      return new Promise<void>((resolve, reject) => {
        resolve(undefined);
      });
    },
    isEnabled: hasWidget
  });

  let menu = new Menu({ commands });
  menu.title.label = 'Export Notebook As (no code)...';

  let menu2 = new Menu({ commands });
  menu2.title.label = 'Publish Notebook';


  menu.addItem({command: export_pdf});
  menu.addItem({command: export_html});
  menu2.addItem({command: publish});

  if (mainMenu) {
    mainMenu.fileMenu.addGroup([{ type:'submenu', submenu: menu }, { type:'submenu', submenu: menu2 }], 10);
  }


  // Add the command to the palette.
  palette.addItem({command: export_pdf, category: 'Lantern'});
  palette.addItem({command: export_html, category: 'Lantern'});
  palette.addItem({command: publish, category: 'Lantern'});
};


export default extension;
