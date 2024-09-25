# CommandChrome

## Natural Language Interface to Chrome Extension API

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 18.2.5.

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The application will automatically reload if you change any of the source files.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory.

## Running unit tests

Run `npm test` to execute the unit tests via [Jest](https://jestjs.io/).

## Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via a platform of your choice. To use this command, you need to first add a package that implements end-to-end testing capabilities.

## To fetch and pull all branches from a remote Git repository, you can follow these steps

1. Fetch all remote branches:

   ```sh
   git fetch --all
   ```

    This command downloads all branches and their commits from the remote repository without merging them into your local branches.

2. Set up tracking for all remote branches

   ```sh
   git branch -r | grep -v '\->' | sed "s,\x1B\[[0-9;]*[a-zA-Z],,g" | while read remote; do git branch --track "${remote#origin/}" "$remote"; done
   ```

   This command creates local branches that track their remote counterparts.

3. Pull all branches

   ```sh
   git pull --all
   ```

   This command fetches and merges changes from all remote branches into their corresponding local branches.

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI Overview and Command Reference](https://angular.dev/tools/cli) page.
