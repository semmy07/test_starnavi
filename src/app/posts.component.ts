import { Component } from '@angular/core';
import {WebService} from "./web.service";

@Component({
  selector: 'app-posts',
  template: `
    <mat-card>
      <mat-card-content>
        <!--<mat-input-container>-->
          <input [(ngModel)]="text">
        <!--</mat-input-container>-->
        <mat-card-actions>
          <button (click)="createPost()" mat-button color="primary">Create post</button>
        </mat-card-actions>
      </mat-card-content>
    </mat-card> 
  `,
  styleUrls: ['./app.component.css']
})
export class PostsComponent {
  constructor(private webService: WebService) {}

  text = '';

  createPost() {

  }
}
