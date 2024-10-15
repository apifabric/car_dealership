import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Part-card.component.html',
  styleUrls: ['./Part-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Part-card]': 'true'
  }
})

export class PartCardComponent {


}