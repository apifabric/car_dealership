import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {DEALERSHIPEMPLOYEE_MODULE_DECLARATIONS, DealershipEmployeeRoutingModule} from  './DealershipEmployee-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    DealershipEmployeeRoutingModule
  ],
  declarations: DEALERSHIPEMPLOYEE_MODULE_DECLARATIONS,
  exports: DEALERSHIPEMPLOYEE_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class DealershipEmployeeModule { }