import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DealershipEmployeeHomeComponent } from './home/DealershipEmployee-home.component';
import { DealershipEmployeeNewComponent } from './new/DealershipEmployee-new.component';
import { DealershipEmployeeDetailComponent } from './detail/DealershipEmployee-detail.component';

const routes: Routes = [
  {path: '', component: DealershipEmployeeHomeComponent},
  { path: 'new', component: DealershipEmployeeNewComponent },
  { path: ':id', component: DealershipEmployeeDetailComponent,
    data: {
      oPermission: {
        permissionId: 'DealershipEmployee-detail-permissions'
      }
    }
  }
];

export const DEALERSHIPEMPLOYEE_MODULE_DECLARATIONS = [
    DealershipEmployeeHomeComponent,
    DealershipEmployeeNewComponent,
    DealershipEmployeeDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DealershipEmployeeRoutingModule { }