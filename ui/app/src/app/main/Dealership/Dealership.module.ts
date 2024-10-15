import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {DEALERSHIP_MODULE_DECLARATIONS, DealershipRoutingModule} from  './Dealership-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    DealershipRoutingModule
  ],
  declarations: DEALERSHIP_MODULE_DECLARATIONS,
  exports: DEALERSHIP_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class DealershipModule { }