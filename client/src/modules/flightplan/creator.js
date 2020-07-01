import React, { useState } from 'react';
import { makeStyles } from '@material-ui/core/styles'
import { Typography, TextField, Grid, Button } from '@material-ui/core'


const FlightPlanCreator = () => {
    const classes = useStyles()   

    return (
        <Grid container spacing={3}>
            <Grid item xs={12}>
                <div className={classes.root}>
                    <div className={classes.formRow}>
                        <TextField
                        label="OPTIONAL FLIGHT NOTES"                                     
                        className={classes.textField}                
                        margin="normal"
                        InputLabelProps={{ shrink: true }}
                        variant="outlined"
                        />
                    </div>
                    <div className={classes.formRow}>
                        <TextField
                        label="CALLSIGN"                               
                        className={classes.textField}                
                        margin="normal"
                        InputLabelProps={{ shrink: true }}
                        variant="outlined"
                        />
                        <TextField
                        label="AIRCRAFT TYPE"                        
                        className={classes.textField}                
                        margin="normal"
                        InputLabelProps={{ shrink: true }}
                        variant="outlined"
                        />                
                    </div>
                    <div className={classes.formRow}>
                        <TextField
                        label="ORIGIN AIRPORT"                               
                        className={classes.textField}                
                        margin="normal"
                        InputLabelProps={{ shrink: true }}
                        variant="outlined"
                        />
                        <TextField
                        label="DESTINATION AIRPORT"                               
                        className={classes.textField}                
                        margin="normal"
                        InputLabelProps={{ shrink: true }}
                        variant="outlined"
                        />  
                        <TextField
                        label="DEPARTURE/START TIME"                        
                        className={classes.textField}                
                        margin="normal"
                        InputLabelProps={{ shrink: true }}
                        variant="outlined"
                        />               
                    </div>
                    <div className={classes.formRow}>
                        <TextField
                        label="CRUISING SPEED"                               
                        className={classes.textField}                
                        margin="normal"
                        InputLabelProps={{ shrink: true }}
                        variant="outlined"
                        />
                        <TextField
                        label="CRUISING FL"
                        className={classes.textField}                
                        margin="normal"
                        InputLabelProps={{ shrink: true }}
                        variant="outlined"
                        />                
                    </div>
                    <div className={classes.formRow}>
                        <TextField
                        label="ROUTE TYPE"                        
                        className={classes.textField}                
                        margin="normal"
                        InputLabelProps={{ shrink: true }}
                        variant="outlined"
                        />  
                        <TextField
                        id="filled-full-width"
                        label="ROUTES"
                        className={classes.textFieldWide}
                        InputLabelProps={{ shrink: true }}
                        variant="outlined"
                        multiline
                        rows={4}                        
                        />
                    </div>
                    <div className={classes.textField}>
                        <Button variant="contained" color="primary">CREATE</Button>
                    </div>
                </div> 
            </Grid>
        </Grid>  
    )
}

export default FlightPlanCreator



/**
 * CSS Rules
 */

const useStyles = makeStyles((theme) => ({
    root: {
        // display: 'flex',
        // flexDirection: 'column',
        // flexWrap: 'wrap',
    },
    formRow: {
        marginBottom: theme.spacing(2),
    },
    textField: {
        marginLeft: theme.spacing(2),
        marginRight: theme.spacing(2),
        width: '25ch',
    }, 
    textFieldWide: {
        margin: theme.spacing(2),        
        width: '75ch',
    },   
}))