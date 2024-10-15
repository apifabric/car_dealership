import { MenuRootItem } from 'ontimize-web-ngx';

import { CarInventoryCardComponent } from './CarInventory-card/CarInventory-card.component';

import { CarModelCardComponent } from './CarModel-card/CarModel-card.component';

import { CustomerCardComponent } from './Customer-card/Customer-card.component';

import { DealershipCardComponent } from './Dealership-card/Dealership-card.component';

import { DealershipEmployeeCardComponent } from './DealershipEmployee-card/DealershipEmployee-card.component';

import { EmployeeCardComponent } from './Employee-card/Employee-card.component';

import { InventoryPartCardComponent } from './InventoryPart-card/InventoryPart-card.component';

import { MaintenanceCardComponent } from './Maintenance-card/Maintenance-card.component';

import { PartCardComponent } from './Part-card/Part-card.component';

import { SaleCardComponent } from './Sale-card/Sale-card.component';

import { ServiceCardComponent } from './Service-card/Service-card.component';

import { SupplierCardComponent } from './Supplier-card/Supplier-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'CarInventory', name: 'CARINVENTORY', icon: 'view_list', route: '/main/CarInventory' }
    
        ,{ id: 'CarModel', name: 'CARMODEL', icon: 'view_list', route: '/main/CarModel' }
    
        ,{ id: 'Customer', name: 'CUSTOMER', icon: 'view_list', route: '/main/Customer' }
    
        ,{ id: 'Dealership', name: 'DEALERSHIP', icon: 'view_list', route: '/main/Dealership' }
    
        ,{ id: 'DealershipEmployee', name: 'DEALERSHIPEMPLOYEE', icon: 'view_list', route: '/main/DealershipEmployee' }
    
        ,{ id: 'Employee', name: 'EMPLOYEE', icon: 'view_list', route: '/main/Employee' }
    
        ,{ id: 'InventoryPart', name: 'INVENTORYPART', icon: 'view_list', route: '/main/InventoryPart' }
    
        ,{ id: 'Maintenance', name: 'MAINTENANCE', icon: 'view_list', route: '/main/Maintenance' }
    
        ,{ id: 'Part', name: 'PART', icon: 'view_list', route: '/main/Part' }
    
        ,{ id: 'Sale', name: 'SALE', icon: 'view_list', route: '/main/Sale' }
    
        ,{ id: 'Service', name: 'SERVICE', icon: 'view_list', route: '/main/Service' }
    
        ,{ id: 'Supplier', name: 'SUPPLIER', icon: 'view_list', route: '/main/Supplier' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    CarInventoryCardComponent

    ,CarModelCardComponent

    ,CustomerCardComponent

    ,DealershipCardComponent

    ,DealershipEmployeeCardComponent

    ,EmployeeCardComponent

    ,InventoryPartCardComponent

    ,MaintenanceCardComponent

    ,PartCardComponent

    ,SaleCardComponent

    ,ServiceCardComponent

    ,SupplierCardComponent

];