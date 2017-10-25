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
  ICommandPalette, IMainMenu
} from '@jupyterlab/apputils';

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

  let menu = new Menu({ commands });
  let menu2 = new Menu({ commands });
  let menu3 = new Menu({ commands });
  menu.title.label = 'Lantern';
  menu2.title.label = 'Export to ...';
  menu3.title.label = 'No Code';

  menu3.addItem({command: export_pdf});
  menu3.addItem({command: export_html});
  menu3.addItem({type: 'separator'});
  menu2.addItem({type: 'submenu', submenu:menu3});
  menu.addItem({type: 'submenu', submenu:menu2});
  mainMenu.addMenu(menu);
  // Add the command to the palette.
  palette.addItem({command: export_pdf, category: 'Lantern'});
  palette.addItem({command: export_pdf, category: 'Lantern'});
};


export default extension;
