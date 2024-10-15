import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Maintenance-card.component.html',
  styleUrls: ['./Maintenance-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Maintenance-card]': 'true'
  }
})

export class MaintenanceCardComponent {


}