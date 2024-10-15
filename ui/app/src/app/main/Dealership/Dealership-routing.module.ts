import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DealershipHomeComponent } from './home/Dealership-home.component';
import { DealershipNewComponent } from './new/Dealership-new.component';
import { DealershipDetailComponent } from './detail/Dealership-detail.component';

const routes: Routes = [
  {path: '', component: DealershipHomeComponent},
  { path: 'new', component: DealershipNewComponent },
  { path: ':id', component: DealershipDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Dealership-detail-permissions'
      }
    }
  },{
    path: ':dealership_id/DealershipEmployee', loadChildren: () => import('../DealershipEmployee/DealershipEmployee.module').then(m => m.DealershipEmployeeModule),
    data: {
        oPermission: {
            permissionId: 'DealershipEmployee-detail-permissions'
        }
    }
}
];

export const DEALERSHIP_MODULE_DECLARATIONS = [
    DealershipHomeComponent,
    DealershipNewComponent,
    DealershipDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DealershipRoutingModule { }