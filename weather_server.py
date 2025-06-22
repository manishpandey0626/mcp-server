from fastmcp import FastMCP

mcp = FastMCP("My Weather Server")

@mcp.tool("weather")
async def weather(location: str) -> str:
    """
    Get the current weather for a given location.
    
    Args:
        location (str): The name of the location to get the weather for.
        
    Returns:
        str: A string describing the current weather in the specified location.
    """
    # Simulated weather data for demonstration purposes
    weather_data = {
        "New York": "Sunny, 25°C",
        "Los Angeles": "Cloudy, 22°C",
        "Chicago": "Rainy, 18°C"
    }
    
    return weather_data.get(location, "Weather data not available for this location.")


if __name__ == "__main__":
    mcp.run(transport="streamable-http")