import React, { useState } from 'react';
import { makeStyles } from '@material-ui/core/styles'
import { AppBar, Toolbar, Typography, Grid, List, ListItem, ListItemText } from '@material-ui/core'
import { grey } from '@material-ui/core/colors';


import FlightPlan from '../modules/flightplan/index'
import ScenarioEditor from '../modules/scenarioeditor/index'


const Modules = [
    <FlightPlan />,
    <ScenarioEditor />
] 


const SimHome = () => {
    const classes = useStyles()
    const [selectedIndex, setSelectedIndex] = useState(0)
    
    const handleListItemClick = (e, index) => {        
        setSelectedIndex(index);
    }  

    return (
        <div className={classes.root}>
            <AppBar position="static" className={classes.appBar}>
                <Toolbar>
                    <Typography variant="h6" className={classes.title}>
                        DATA PREPARATION - Intelligent Air Traffic Simulator (iSIM)
                    </Typography>              
                </Toolbar>
            </AppBar>
            <Grid container spacing={5}>
                {/* Left Sidebar */}
                <Grid item xs={4} lg={2}>
                    <div className={classes.sidePanel}>
                        <List compoent="nav">
                            <ListItem                            
                                button
                                selected={selectedIndex === 0}
                                onClick={(e) => handleListItemClick(e, 0)}
                                >
                                <ListItemText primary="Flight Plan" />
                            </ListItem>
                            <ListItem                            
                                button
                                selected={selectedIndex === 1}
                                onClick={(e) => handleListItemClick(e, 1)}
                                >
                                <ListItemText primary="Scenario Editor" />
                            </ListItem>
                        </List>                        
                    </div>
                </Grid>
                
                {/* Main content */}
                <Grid item xs={8} lg={10}>
                    <div className={classes.moduleContent}>
                        {Modules[selectedIndex]}
                    </div>                    
                </Grid>                
            </Grid>
        </div>
      );    
}

export default SimHome


/**
 * CSS Rules
 */

const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
        color: grey[800]
    },
    appBar : {
        backgroundColor: grey[800],
    },
    title: {
        flexGrow: 1,
    },
    sidePanel : {
        paddingRight: 50,
    },
    moduleContent : {
        padding: 10
    }
}))