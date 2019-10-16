try({
      <do something>
    }, silent = TRUE)  # WARN?
    if ( "try-error" %in% class(result) ) {
      err_msg <- geterrmessage()
      if ( stringr::str_detect(err_msg, "cannot open the connection") ) {
        print(paste0(filepath, " not found. Run installGoesGrids()." )  )
        stop()
      }
    } else {
      print(paste0("Stacked hour: ", hour, " UTC"))
    }
  }
  
checkFile <- function(fullPath) {

  status <- file.exists(fullPath)
  
  return status
}

# ------------------------------------#

goesaodc_isGoesProjection <- function(nc)
  {
  projection <- goesaodc_getProjection(nc)
  satelliteDataDir <- getSatelliteDataDir()
  tryCatch(
    expr = {
      goesEastGrid <- get(load(file.path(satelliteDataDir, "goesEastGrid.rda")))
      goesWestGrid <- get(load(file.path(satelliteDataDir, "goesWestGrid.rda")))
      isGoesEast <- all(unlist(projection) == unlist(goesEastGrid$projection))
      isGoesWest <- all(unlist(projection) == unlist(goesWestGrid$projection))
    },
    error = function(e){
      stop(e)
    },
    warning = function(w){
      stop(w)
    }
  )
  return(isGoesEast || isGoesWest)
  }