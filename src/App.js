import logo from './logo.svg';
import { fade, makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import IconButton from '@material-ui/core/IconButton';
import Typography from '@material-ui/core/Typography';
import InputBase from '@material-ui/core/InputBase';
import Badge from '@material-ui/core/Badge';
import MenuItem from '@material-ui/core/MenuItem';
import Menu from '@material-ui/core/Menu';
import MenuIcon from '@material-ui/icons/Menu';
import SearchIcon from '@material-ui/icons/Search';
import AccountCircle from '@material-ui/icons/AccountCircle';
import MailIcon from '@material-ui/icons/Mail';
import NotificationsIcon from '@material-ui/icons/Notifications';
import MoreIcon from '@material-ui/icons/MoreVert';
import './App.css';
import Header from './Components/Header/Header'
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';
import '@material-ui/core/';
import Carousel from 'react-bootstrap/Carousel';
import HomePage from './Components/HomePage';
import { BrowserRouter as Router,Route,Switch,Link } from 'react-router-dom';
import Error from './Components/Errors/Error';
import Testing from './Components/Testing/Testing';
import SignInSide from './Components/Authintication/SignInSide';
import SignUp from './Components/Authintication/SignUp';
import Checkout from './Components/PymentProcess/Checkout';
import Blog from './Components/Blogs/Blogs';
import RecipeReviewCard from './Components/SurfaceInputs/RecipeReviewCard';
import Carosoul_Inputs from './Components/SurfaceInputs/Carosoul_Inputs';
import ImageGridList from './Components/SurfaceInputs/ImageGridList';
import StickyFooter from './Components/Footer/StickyFooter';
import LeftBar from './Components/SurfaceInputs/LeftBar';
import Contactus from './Components/ContactUs/Contactus';
import Cindex from './Components/ContactUs/Cindex';
import AboutIndex from './Components/Aboutus/AboutIndex';

function App() {
  return (
    <Router>
    <div className="App">
       
  
    <Switch>
      <Route exact path='/'><HomePage/></Route> 
      <Route exact path='/testing' component={Testing}/>
      <Route exact path='/signin' component={SignInSide}/>
      <Route exact path='/signup' component={SignUp}/>
      <Route exact path='/checkout' component={Checkout}/>
      <Route exact path='/blogs' component={Blog}/>
      <Route exact path='/carosoul' component={Carosoul_Inputs}/>
      <Route exact path='/grids' component={StickyFooter}/>
      <Route exact path='/leftbars' component={LeftBar}/>
      <Route exact path='/contactus' component={Cindex}/>
      <Route exact path='/aboutus' component={AboutIndex}/>


      

      

     


    





     
      <Route exact path='*' component={Error}/>


    </Switch>
    </div>
    </Router>
  );
}

export default App;