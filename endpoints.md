## Summary
This page documents any quirks in the APIs that are worth documenting and ideally
fixing or clarifying in either the API docs, or the API implementations.

Any quirks that affect the runtime behavior and expectations could be
good opportunities for adding in warning messages in the client.

## [ETH Gas Station](https://web.archive.org/web/20210602120344/https://docs.defipulse.com/api-docs-by-provider/egs)

## [Rek.to](https://web.archive.org/web/20210602120354/https://docs.defipulse.com/api-docs-by-provider/rek.to)

- [`/events`](https://web.archive.org/web/20210602120843/https://docs.defipulse.com/api-docs-by-provider/rek.to/events)
    - It looks like `minSize` and `symbol` params do not work, however, we can go to app.rek.to and clearly see these query params working in a network request there.
    
- [`/top10`](https://web.archive.org/web/20210602120845/https://docs.defipulse.com/api-docs-by-provider/rek.to/untitled)
    - It looks like `minSize` and `symbol` params do not work.

- [docs](https://web.archive.org/web/20210602120843/https://docs.defipulse.com/api-docs-by-provider/rek.to/events)
    - docs point to `defiupulse` instead of `defipulse`.

## [Pools.fyi](https://web.archive.org/web/20210602120320/https://docs.defipulse.com/api-docs-by-provider/pools.fyi)

- [`/returns`](https://web.archive.org/web/20210602121958/https://docs.defipulse.com/api-docs-by-provider/pools.fyi/returns-by-exchange)
    - This endpoint returns ~30 days of returns data for a particular *liquidity pool* address over time,
      for example, UNI-V2 ETH/GRT.
        - The endpoint will *not* return data across AMMs for an individual token address, like GRT or ETH.
    - The docs' "Request" section could be updated to include `address` as a path param.

- [`/liquidity`](https://web.archive.org/web/20210602124621/https://docs.defipulse.com/api-docs-by-provider/pools.fyi/pool-liquidity)
    - The use of `v0` in the URL is not a typo, even though this is the only Pools.fyi endpoint that uses this `v0` path.

- [`/exchange`](https://web.archive.org/web/20210602124630/https://docs.defipulse.com/api-docs-by-provider/pools.fyi/single-exchange)
    - The docs currently point to an invalid base URL; the same base URL as the other endpoints is the true one.

## [DeFi Pulse](https://web.archive.org/web/20210602120334/https://docs.defipulse.com/api-docs-by-provider/defi-pulse-data)

## [DEX.AG](https://web.archive.org/web/20210602120338/https://docs.defipulse.com/api-docs-by-provider/dex.ag)

- [`/price`](https://web.archive.org/web/20210602120306/https://docs.defipulse.com/api-docs-by-provider/dex.ag/untitled)
    - `fromAmount` and `toAmount` are exclusive options.
    - Both of `fromToken` and `toToken` are required.
    - The API docs specify that `dex` is optional, but it appears to be required in order to work.
    - `discluded` works but seems unable to exclude some DEXes -- specifically, AG appears at the end of the response array, and cannot be excluded when tried with `?disclude=ag`.