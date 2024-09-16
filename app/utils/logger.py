import logging 
def setup_logger():
    """
    This function sets up a logger with the specified configuration.

    Parameters:
    None

    Returns:
    logger (logging.Logger): A logger object with the specified configuration.
    """
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')
    return logging.getLogger(__name__)

