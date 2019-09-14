import React, {Component} from 'react';

import PostMinInfo from "./PostMinInfo.jsx";
import PostMaxInfo from "./PostMaxInfo.jsx";

class PostsList extends Component {// Блок, в котором будут рисоваться посты
    constructor(props){
        super(props);
         this.state = {
             posts: [],
         }
    }
    render() {
        if(!this.state.posts.length) return null;
        const posts = this.state.posts.map((post, index) => {
           return <PostMinInfo key={index} {...post}/>}
        );
        this.state.posts.map((post, index) => {
            return <PostMaxInfo key={index} {...post}/>}
        );
        return (
            <>
                <div className="descriptions">
                    <div className="descriptions-left">
                        <div className="description">
                            <h1>
                                Проекты
                            </h1>
                            <p>
                                В этом разделе представлены интересные проекты, подобранные по вашим предпочтениям
                            </p>
                        </div>
                        <div className="tegs">
                            {/*TODO Сделать отдельный компонент для тегов*/}
                        </div>
                    </div>
                    <div className="descriptions-right">
                        <img className="descriptions-right" src="https://github.com/fckxorg/ASI_Backend/blob/master/static/big_logo.png?raw=true" alt="USER_IMG"/>
                    </div>
                </div>
                <div className='cards'>
                    {posts}
                </div>
            </>
        );
    }
    componentDidMount() {
        fetch('api/pitch/get/new/')
            .then(response => response.json())
            .then(data => this.setState({posts: data}))

    }
}

export default PostsList;
