import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'CarInventory-new',
  templateUrl: './CarInventory-new.component.html',
  styleUrls: ['./CarInventory-new.component.scss']
})
export class CarInventoryNewComponent {
  @ViewChild("CarInventoryForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}