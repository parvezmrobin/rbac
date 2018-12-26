import React, {Component} from 'react';
import './css/bootstrap.css';
import './css/site.css';

class App extends Component {
    render() {
        const props = this.props;

        return (
            <div className="container-fluid" id="vm">
                <nav className="navbar navbar-expand-sm navbar-dark bg-dark fixed-top">
                    <a className="navbar-brand ml-sm-4 pl-sm-1" href="/">RBAC</a>
                    <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbar-rbac"
                            aria-controls="navbar-rbac" aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse" id="navbar-rbac">
                        <form className="form-inline w-100">
                            <input className="form-control search w-100 mx-sm-3" type="text" placeholder="Search"
                                   aria-label="Search"/>
                        </form>

                        <ul className="navbar-nav ml-auto">
                            {/*<div v-if="user">*/}
                            {/*<li className="nav-item text-nowrap pr-2">*/}
                            {/*<span className="navbar-text">Hi <span>{props.user.username}</span>!</span>*/}
                            {/*</li>*/}
                            {/*<li className="nav-item text-nowrap">*/}
                            {/*<a className="nav-link" v-on:click="logout" href="#">Logout</a>*/}
                            {/*</li>*/}
                            {/*</div>*/}
                            <li className="nav-item text-nowrap">
                                <a className="nav-link" href="#">Login</a>
                            </li>
                            <li className="nav-item text-nowrap">
                                <a className="nav-link" href="#">Register</a>
                            </li>
                        </ul>
                    </div>
                </nav>

                <div className="container-fluid mt-5 pt-2">
                    <div className="row">
                        <nav className="col-md-3 col-lg-2 mt-5" id="sidebar">
                            <ul className="nav flex-column">
                                <li className="nav-item">
                                    <a className="nav-link" id="nav-dash" href="#">
                                        <span data-feather="home"></span>
                                        Dashboard
                                    </a>
                                </li>
                                <li className="nav-item">
                                    <a className="nav-link" id="nav-user" href="#">
                                        <span data-feather="user"></span>
                                        Users
                                    </a>
                                </li>
                                <li className="nav-item">
                                    <a className="nav-link" id="nav-role" href="#">
                                        <span data-feather="briefcase"></span>
                                        Roles
                                    </a>
                                </li>
                                <li className="nav-item">
                                    <a className="nav-link" id="nav-permission"
                                       href="#">
                                        <span data-feather="globe"></span>
                                        Permissions
                                    </a>
                                </li>
                            </ul>
                        </nav>

                        <main role="main" className="col-md-9 col-lg-10 px-5">
                            {props.content}
                        </main>
                    </div>
                </div>
            </div>
        );
    }
}

export default App;
