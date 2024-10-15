import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './CarModel-card.component.html',
  styleUrls: ['./CarModel-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.CarModel-card]': 'true'
  }
})

export class CarModelCardComponent {


}