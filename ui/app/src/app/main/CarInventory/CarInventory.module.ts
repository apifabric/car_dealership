import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {CARINVENTORY_MODULE_DECLARATIONS, CarInventoryRoutingModule} from  './CarInventory-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    CarInventoryRoutingModule
  ],
  declarations: CARINVENTORY_MODULE_DECLARATIONS,
  exports: CARINVENTORY_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class CarInventoryModule { }