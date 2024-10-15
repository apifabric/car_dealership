import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Dealership-card.component.html',
  styleUrls: ['./Dealership-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Dealership-card]': 'true'
  }
})

export class DealershipCardComponent {


}