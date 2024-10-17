A recycling website where users can donate items to designated locations, and will be awarded points according to how much they donate. 

Public-side:
- Points counter
- Exchange page (exchange points for rewards w/ partnering groups/companies)
- List of collection points

Staff-side:
- View database entries
- View all collection points, sorted by order of importance (how full each collection point is)
- View points transaction history
- Modify points for individual users


Database structure:
- Accounts
    - Username
    - Password - hashed
    - Mobile no.
    - Points
    - Privilege
- Internal
    - Transactions
    - Collection points

Endpoints:
- Public:
    - /api/points/  (GET)
    - /api/rewards/list  (GET)
    - /api/rewards/exchange  (POST)
    - /api/collection/list  (GET)
- Internal:
    - /api/internal/accounts  (GET)
    - /api/internal/transactions  (GET)
    - /api/internal/collection  (GET)
    - /api/internal/transaction-history/<username>  (GET)
    - /api/internal/accounts/<username>/points  (PUT)