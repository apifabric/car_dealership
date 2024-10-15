import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { InventoryPartHomeComponent } from './home/InventoryPart-home.component';
import { InventoryPartNewComponent } from './new/InventoryPart-new.component';
import { InventoryPartDetailComponent } from './detail/InventoryPart-detail.component';

const routes: Routes = [
  {path: '', component: InventoryPartHomeComponent},
  { path: 'new', component: InventoryPartNewComponent },
  { path: ':id', component: InventoryPartDetailComponent,
    data: {
      oPermission: {
        permissionId: 'InventoryPart-detail-permissions'
      }
    }
  }
];

export const INVENTORYPART_MODULE_DECLARATIONS = [
    InventoryPartHomeComponent,
    InventoryPartNewComponent,
    InventoryPartDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class InventoryPartRoutingModule { }