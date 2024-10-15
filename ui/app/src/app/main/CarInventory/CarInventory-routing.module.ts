import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CarInventoryHomeComponent } from './home/CarInventory-home.component';
import { CarInventoryNewComponent } from './new/CarInventory-new.component';
import { CarInventoryDetailComponent } from './detail/CarInventory-detail.component';

const routes: Routes = [
  {path: '', component: CarInventoryHomeComponent},
  { path: 'new', component: CarInventoryNewComponent },
  { path: ':id', component: CarInventoryDetailComponent,
    data: {
      oPermission: {
        permissionId: 'CarInventory-detail-permissions'
      }
    }
  },{
    path: ':inventory_id/InventoryPart', loadChildren: () => import('../InventoryPart/InventoryPart.module').then(m => m.InventoryPartModule),
    data: {
        oPermission: {
            permissionId: 'InventoryPart-detail-permissions'
        }
    }
},{
    path: ':inventory_id/Maintenance', loadChildren: () => import('../Maintenance/Maintenance.module').then(m => m.MaintenanceModule),
    data: {
        oPermission: {
            permissionId: 'Maintenance-detail-permissions'
        }
    }
},{
    path: ':inventory_id/Sale', loadChildren: () => import('../Sale/Sale.module').then(m => m.SaleModule),
    data: {
        oPermission: {
            permissionId: 'Sale-detail-permissions'
        }
    }
}
];

export const CARINVENTORY_MODULE_DECLARATIONS = [
    CarInventoryHomeComponent,
    CarInventoryNewComponent,
    CarInventoryDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CarInventoryRoutingModule { }