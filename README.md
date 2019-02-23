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
   1. - [ ] Convert region ID to name
   1. - [ ] Convert region name to ID
   1. - [ ] Get adjacent region names for a region by name
   1. - [ ] Get adjacent region IDs for a region by name
   1. - [ ] Get adjacent region ID/name pairs for a region by name
   1. - [ ] Get adjacent region names for a region by ID
   1. - [ ] Get adjacent region IDs for a region by ID
   1. - [ ] Get adjacent region ID/name pairs for a region by ID
   1. - [ ] Get list of system IDs for a region by ID
   1. - [ ] Get list of system names for a region by ID
   1. - [ ] Get list of system ID/name pairs for a region by ID

1. Systems

   1. - [ ] Convert system ID to name
   1. - [ ] Convert system name to ID

1. Market Buy Orders

   1. - [ ] Get a list of buy orders for an item ID by region ID
   1. - [ ] Get a list of buy orders for an item ID by region name
   1. - [ ] Get a list of buy orders for an item name by region ID
   1. - [ ] Get a list of buy orders for an item name by region name
   1. - [ ] Get a list of buy orders for an item market group ID by system ID
   1. - [ ] Get a list of buy orders for an item market group ID by system name
   1. - [ ] Get a list of buy orders for an item market group name by system ID
   1. - [ ] Get a list of buy orders for an item market group name by system name

1. Market Sell Orders

   1. - [ ] Get a list of sell orders for an item ID by region name
   1. - [ ] Get a list of sell orders for an item ID by region ID
   1. - [ ] Get a list of sell orders for an item name by region ID
   1. - [ ] Get a list of sell orders for an item name by region name
   1. - [ ] Get a list of sell orders for an item market group ID by system ID
   1. - [ ] Get a list of sell orders for an item market group ID by system name
   1. - [ ] Get a list of sell orders for an item market group name by system ID
   1. - [ ] Get a list of sell orders for an item market group name by system name

1. Item Details

   1. - [ ] Get a list of item details for an item ID
   1. - [ ] Get a list of item details for an item name
   1. - [ ] Get volume of item by ID
   1. - [ ] Get volume of item by name
   1. - [ ] Get description of item by ID
   1. - [ ] Get description of item by name
   1. - [ ] Get item market group of item by ID (redirect to /api/item)
   1. - [ ] Get item market group of item by name
   1. - [ ] Get skill requirements of item by ID
   1. - [ ] Get skill requirements of item by namy
   1. - [ ] Get manufacturing requirements of item by ID (recursive?)
   1. - [ ] Get manufacturing requirements of item by name (recursive?)
	
