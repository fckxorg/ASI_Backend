import React, {Component} from 'react';

import PostsList from "../components/Posts/PostsList.jsx";

class Posts extends Component {// Это страница в которой будут все посты
    render() {
        return (
            <>
                {(!this.props.children) ? <PostsList/> : (this.props.children)}
            </>
        );
    }
}

export default Posts;
