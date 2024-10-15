import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './InventoryPart-card.component.html',
  styleUrls: ['./InventoryPart-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.InventoryPart-card]': 'true'
  }
})

export class InventoryPartCardComponent {


}