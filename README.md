> May As Well Learn MarkDown While I'm At It (tm)


# eveBackend

This script will hold all backend code for the EVE Market Analyser.
It will be hostable (hopefully) on nginx or apache, once finished.

## Requirements:
* locally hosted mysql database for the SDE
* python3
* flask
* mysql-connector

The backend will be able to, for a particular location, search the
region and adjacent regions for items and find price disparities. 
For each disparity, it should be able to calculate the most profitable
buy and sell pair using ISK/jump, required collateral, volume, and 
low-sec risk. Limits for the jump count should be an option to avoid
huge treks.
## TODO:
#### Basic API endpoints
###### Use blueprints / separate api parts into files

1. Items
   1. getItemName
      1. - [x] ByItemID
   1. getItemID
      1. - [x] ByItemName
   1. getItemIDs
      1. - [x] ByMarketGroupID
      1. - [x] ByMarketGroupName
   1. getItemNames
      1. - [x] ByMarketGroupID
      1. - [x] ByMarketGroupName
   1. getItems (ID,name) **More information may be provided by this endpoint later**
      1. - [x] ByMarketGroupID
      1. - [x] ByMarketGroupName

1. Market Groups
   1. getMarketGroupID
      1. - [x] ByMarketGroupName
      1. - [x] ByItemID
      1. - [x] ByItemName
   1. getMarketGroupName
      1. - [x] ByMarketGroupID
      1. - [x] ByItemID
      1. - [x] ByItemName
   1. getMarketGroup (ID,name) **More information may be provided by this endpoint later**
      1. - [x] ByItemID
      1. - [x] ByItemName
   1. getMarketGroupHeirarchy
      1. - [x] ByItemID
      1. - [x] ByItemName
      1. - [x] ByMarketGroupID
      1. - [x] ByMarketGroupName
   
1. Regions
   1. getRegionID
      1. - [x] ByRegionName
   1. getRegionName
      1. - [x] ByRegionID
   1. getAdjacentRegionNames
      1. - [x] ByRegionName
      1. - [x] ByRegionID
   1. getAdjacentRegionIDs
      1. - [x] ByRegionName
      1. - [x] ByRegionID
   1. getAdjacentRegions
      1. - [x] ByRegionName
      1. - [x] ByRegionID

1. Systems
   1. getSystemID
      1. - [x] BySystemName
   1. getSystemName
      1. - [x] BySystemID
   1. getSystemIDs
      1. - [x] ByRegionID
      1. - [x] ByRegionName
   1. getSystemNames
      1. - [x] ByRegionID
      1. - [x] ByRegionName
   1. getSystems
      1. - [x] ByRegionID
      1. - [x] ByRegionName

1. Market Buy Orders
   1. getBuyOrders
      1. ForItemID
         1. - [x] ByRegionID
         1. - [x] ByRegionName
      1. ForItemName
         1. - [x] ByRegionID
         1. - [x] ByRegionName
      1. ForMarketGroupID
         1. - [x] ByRegionID
         1. - [x] ByRegionName
      1. ForMarketGroupName
         1. - [x] ByRegionID
         1. - [x] ByRegionName

1. Market Sell Orders
   1. getSellOrders
      1. ForItemID
         1. - [x] ByRegionID
         1. - [x] ByRegionName
      1. ForItemName
         1. - [x] ByRegionID
         1. - [x] ByRegionName
      1. ForMarketGroupID
         1. - [x] ByRegionID
         1. - [x] ByRegionName
      1. ForMarketGroupName
         1. - [x] ByRegionID
         1. - [x] ByRegionName

1. Item Details
   1. getItemDetails
      1. - [ ] ByItemID
      1. - [ ] ByItemName
   1. getItemVolume
      1. - [ ] ByItemID
      1. - [ ] ByItemName
   1. getItemDescription
      1. - [ ] ByItemID
      1. - [ ] ByItemName
   1. Get description of item by ID
      1. - [ ] ByItemID
      1. - [ ] ByItemName
   1. Get description of item by name
      1. - [ ] ByItemID
      1. - [ ] ByItemName
   1. Get item market group of item by ID (redirect to /api/item)
      1. - [ ] ByItemID
      1. - [ ] ByItemName
   1. Get item market group of item by name
      1. - [ ] ByItemID
      1. - [ ] ByItemName
   1. Get skill requirements of item by ID
      1. - [ ] ByItemID
      1. - [ ] ByItemName
   1. Get skill requirements of item by name
      1. - [ ] ByItemID
      1. - [ ] ByItemName
   1. Get manufacturing requirements of item by ID 
      1. - [ ] ByItemID
      1. - [ ] ByItemName
   1. Get manufacturing requirements of item by name (recursive?)
      1. - [ ] ByItemID
      1. - [ ] ByItemName
	
#### API Calculations
1. ESI Connection (thread)
   1. - [x] Transparent connection to ESI with a single connection for entire app
   1. - [x] Cached results with HTTP 304 support
	    This should be used as the primary caching mechanism. Caching should
	    persist between app restarts.
   1. - [ ] Recovery from exceptions without thread termination
   1. - [x] Graceful thread termination on exit
1. Market Orders (thread)
   1. For each region:
      1. - [x] Get all relevant types through ESI Connection
      1. - [ ] Get daily stats for each type through ESI Connection
      1. - [ ] Recover for exceptions without crashing
   1. For each type:
      1. - [x] Collect the buy and sell orders for each region
      1. Find best x buy-sell pairs with the following considerations:
         1. - [ ] Fewest jumps
         1. - [ ] Minimum collateral % of profit
         1. - [ ] Max profit per cubic metre
	 Basically, the trade with the most profit in the fewest jumps with the
         least collateral should be at the top of the calculated list.
	 Also, this calculation should do both intra and inter region trades.

