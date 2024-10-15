import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Dealership-new',
  templateUrl: './Dealership-new.component.html',
  styleUrls: ['./Dealership-new.component.scss']
})
export class DealershipNewComponent {
  @ViewChild("DealershipForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}