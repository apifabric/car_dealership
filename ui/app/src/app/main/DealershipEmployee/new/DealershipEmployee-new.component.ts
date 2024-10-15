import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'DealershipEmployee-new',
  templateUrl: './DealershipEmployee-new.component.html',
  styleUrls: ['./DealershipEmployee-new.component.scss']
})
export class DealershipEmployeeNewComponent {
  @ViewChild("DealershipEmployeeForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}