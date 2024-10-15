import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {INVENTORYPART_MODULE_DECLARATIONS, InventoryPartRoutingModule} from  './InventoryPart-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    InventoryPartRoutingModule
  ],
  declarations: INVENTORYPART_MODULE_DECLARATIONS,
  exports: INVENTORYPART_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class InventoryPartModule { }