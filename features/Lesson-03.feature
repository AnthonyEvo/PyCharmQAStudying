Feature: Ebay.com regression-02

    Scenario: Validate the search functionality

        Given Navigate to ebay.com
        * Search for Daily Deals in nav
        * Open link Daily Deals in nav
        * Verify Deals in Main and go back to ebay.com

        * Search for Brand Outlet in nav
        #* Open link Brand Outlet in nav
        #* Verify Brand Outlet in section and go back to ebay.com

        * Search for Gift Cards in nav
        * Open link Gift Cards in nav
        * Verify eBay eGift Cards in section and go back to ebay.com

        * Search for Help & Contact in nav
        * Open link Help & Contact in nav
        * Verify Customer Service in header and go back to ebay.com