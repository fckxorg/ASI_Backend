import React, {Component} from 'react';
import {Link} from "react-router";
import PostMinInfo from "../Posts/PostMinInfo.jsx";

class UserInfo extends Component {
    constructor(props) {
        super(props);
        this.state = {
            user: [],
            posts:[],
        }
    }

    componentDidMount() {
        fetch('api/user/0')
            .then(response => response.json())
            .then(data => this.setState({user:data}));
        fetch('api/user/pitch/0')
            .then(response => response.json())
            .then(data => {
                this.setState({posts:data.pitches});
            });
        }

    render() {
        const port = 'http://127.0.0.1:8000';
        const location = <svg className="octicon octicon-location" viewBox="0 0 12 16" version="1.1" width="12"
                             height="16" aria-hidden="true" fill="#f9f9f9">
            <path fill-rule="evenodd"
                  d="M6 0C2.69 0 0 2.5 0 5.5 0 10.02 6 16 6 16s6-5.98 6-10.5C12 2.5 9.31 0 6 0zm0 14.55C4.14 12.52 1 8.44 1 5.5 1 3.02 3.25 1 6 1c1.34 0 2.61.48 3.56 1.36.92.86 1.44 1.97 1.44 3.14 0 2.94-3.14 7.02-5 9.05zM8 5.5c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"></path>
        </svg>;

        const education = <svg xmlns="http://www.w3.org/2000/svg" width="12" height="16" viewBox="0 0 24 24" fill="#f9f9f9"><path d="M20 12.875v5.068c0 2.754-5.789 4.057-9 4.057-3.052 0-9-1.392-9-4.057v-6.294l9 4.863 9-3.637zm-8.083-10.875l-12.917 5.75 12 6.5 11-4.417v7.167h2v-8.25l-12.083-6.75zm13.083 20h-4c.578-1 1-2.5 1-4h2c0 1.516.391 2.859 1 4z"/></svg>;

        const email = <svg className="octicon octicon-mail" viewBox="0 0 14 16" version="1.1" width="14" height="16"
                           aria-hidden="true" fill="#f9f9f9">
            <path fill-rule="evenodd"
                  d="M0 4v8c0 .55.45 1 1 1h12c.55 0 1-.45 1-1V4c0-.55-.45-1-1-1H1c-.55 0-1 .45-1 1zm13 0L7 9 1 4h12zM1 5.5l4 3-4 3v-6zM2 12l3.5-3L7 10.5 8.5 9l3.5 3H2zm11-.5l-4-3 4-3v6z"></path>
        </svg>;

        const posts = this.state.posts.map((post, index) => {
            return <PostMinInfo key={index} {...post}/>}
        );

        return (
            <div className="user-info">
                <div className="user-projects">
                    <h1 className="user-projects-h1">Ваши проекты</h1>
                    <div className="user-cards">
                        {posts}
                    </div>
                </div>
                <div className="user-data">
                    <div className="user-data-absolute">
                        <img className="user-data-img"
                            // src= "data:image/jpeg;base64,"
                            src={this.state.user.avatar}
                             alt=""/>
                            <div className="user-data-settings">
                                <p className="user-data-description"><b>{this.state.user.first_name} {this.state.user.last_name}</b></p>
                                <ul>
                                    <li className="user-data-description">{email} {this.state.user.email}</li>
                                    <li className="user-data-description">{education} {this.state.user.education}</li>
                                    <li className="user-data-description">{location} {this.state.user.residence}</li>
                                </ul>
                            </div>
                            <button className="user-data-btn">Редактировать</button>
                    </div>
                </div>
            </div>
        );
    }
    // componentDidMount() {
    //     fetch('http://jsonplaceholder.typicode.com/users?_limit=10')
    //         .then(response => response.json())
    //         .then(data => this.setState({posts: data}))
    // }
}

export default UserInfo;
