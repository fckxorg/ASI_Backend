import React, {Component} from 'react';

import PostsList from "../components/Posts/PostsList.jsx";

class Posts extends Component {// Это страница в которой будут все посты
    render() {
        console.log(this.props.children);
        return (
            <>
                {/*{(!this.props.children) ? <PostsList/> : (this.props.children)}*/}
                <PostsList/>
            </>
        );
    }
}

export default Posts;
