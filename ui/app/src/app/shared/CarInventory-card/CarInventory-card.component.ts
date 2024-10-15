import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './CarInventory-card.component.html',
  styleUrls: ['./CarInventory-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.CarInventory-card]': 'true'
  }
})

export class CarInventoryCardComponent {


}