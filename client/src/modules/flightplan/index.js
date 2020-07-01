import React, { useState } from 'react';
import { makeStyles } from '@material-ui/core/styles'
import { Typography, Tabs, Tab } from '@material-ui/core'


import FlightPlanCreator from './creator'
import FlightPlanBrowser from './browser'


const TabContent = [ <FlightPlanCreator />, <FlightPlanBrowser /> ]

const FlightPlan = () => {
    const classes = useStyles()    
    const [value, setValue] = React.useState(0);
    const handleChange = (event, newValue) => {        
        setValue(newValue)
    };
    return (
        <div>
            <Typography variant="h5" className={classes.sectionTitle}>Flight plan</Typography>
            <div className={classes.root}>
                <Tabs
                    value={value}
                    onChange={handleChange}
                    indicatorColor="primary"
                    textColor="primary"                    
                    >
                    <Tab label="Create" />
                    <Tab label="Browse" />
                </Tabs>
            </div>
            <div className={classes.tabContent}>
                {TabContent[value]}
            </div>
        </div>
        
    )
}

export default FlightPlan



/**
 * CSS Rules
 */

const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
    },
    sectionTitle: {
        textAlign: "left",
        marginBottom: theme.spacing(2),
        textTransform: "uppercase"
    },
    tabContent: {
        marginTop: theme.spacing(5)
    }
}))