import React, { Component } from 'react'
import axios from "axios"
import Header from "./Header"
import '../styles/profile.css'
import ProfileInfo from "./ProfileInfo"
import ProfilePost from "./ProfilePost"

class Profile extends Component {
    constructor(props) {
        super(props)
        this.state = {
            member: {cover: 'undefined'}
        }
    }

    componentDidMount() {
        axios.get(window.location.origin + '/api/get-member/' + this.props.id).then(res => {
            const member = res.data
            this.setState({member: member})
        })
        document.querySelector('body').style.overflow = "hidden"
    }

    componentWillUnmount() {
        document.querySelector('body').style.overflow = "auto"
    }

    render() {
        if (this.state.member.cover!='undefined') {
            return (
                <main className="profile-page">
                    {this.props.closeWindow ?
                        (<div className="back-arrow" onClick={this.props.closeWindow}>
                            <i className="el-icon-arrow-left"></i>
                        </div>) : null}
                    <Header cover={this.state.member.cover} avatar={this.state.member.avatar}
                            color={this.state.member.color} name={this.state.member.name}/>
                    <div className="content">
                        <div className="col1">
                            <ProfilePost text={this.state.member.post_text} image={this.state.member.post_image}
                                         title={this.state.member.post_title}/>
                        </div>
                        <div className="col2">
                            <ProfileInfo webcite={this.state.member.webcite} email={this.state.member.email}
                                         city={this.state.member.city}/>
                        </div>
                    </div>
                </main>
            )
        } else {
            return (<main className="profile-page"><i className="el-icon-loading loading-icon"></i></main>)
        }
    }
}

export default Profile
