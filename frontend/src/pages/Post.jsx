import React, {Component} from 'react';

import PostMaxInfo from "../components/Posts/PostMaxInfo.jsx";

class Post extends Component {// Это страница которая отображает Полную инфу поста
    constructor(props){
        super(props);
        this.state = {
            post: null,
            user:null
        }
    }
    render() {
        return (
            <>
                {this.state.post ? <PostMaxInfo {...this.state.post} {...this.state.user}/> : null}
            </>
        );
    }
    componentDidMount() {
        fetch(`../api/pitch/${this.props.params.postId}`)
            .then(response => response.json())
            .then(data => this.setState({post: data}));
        fetch('../api/pitch/get/new/')
            .then(response => response.json())
            .then(data => this.setState({user: data}));
    }
}

export default Post;
