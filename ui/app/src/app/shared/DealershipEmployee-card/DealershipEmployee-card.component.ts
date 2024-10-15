import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './DealershipEmployee-card.component.html',
  styleUrls: ['./DealershipEmployee-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.DealershipEmployee-card]': 'true'
  }
})

export class DealershipEmployeeCardComponent {


}