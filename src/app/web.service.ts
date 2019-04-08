import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';

@Injectable({ providedIn: 'root' })
export class WebService {
    BASE_URL = 'http://127.0.0.1';
    constructor(private http: HttpClient) {}

    getPosts() {
      return this.http.get(this.BASE_URL).toPromise();
    }

    createPost(data) {
      return this.http.post(this.BASE_URL, data).toPromise();
    }
}
