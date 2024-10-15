import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'InventoryPart-new',
  templateUrl: './InventoryPart-new.component.html',
  styleUrls: ['./InventoryPart-new.component.scss']
})
export class InventoryPartNewComponent {
  @ViewChild("InventoryPartForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}