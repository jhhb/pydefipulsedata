# Overview

An unofficial Python SDK for the [DeFi Pulse Data](https://docs.defipulse.com/) project and
each of its partner service providers. This project provides a lightweight Python
client for each service provider.

Currently, the DeFi Pulse Data service providers include:
- [DeFi Pulse](https://defipulse.com/)
- [ETH Gas Station](https://ethgasstation.info/)
- [DEX.AG](https://dex.ag/)
- [Rek.to](https://app.rek.to/)
- [Pools.fyi](https://pools.fyi/#/)

The goals of this package are to empower Python programmers to make use of DeFi Pulse Data services,
to enrich the broader DeFi developer ecosystem, and to reduce overall developer effort by providing
a packaged developer SDK so that developers do not need to reinvent the wheel for each project they make.

This project bears no official relationship to the DeFi Pulse Data project, or the
[Concourse Open Community](https://concourseopen.com/) project.

# Setup

## Requirements

* Python 3.7+

## Installation

Install it directly into an activated virtual environment:

```text
$ pip install defipulsedata
```

or add it to your [Poetry](https://poetry.eustace.io/) project:

```text
$ poetry add defipulsedata
```

# Usage

After installation, the package can imported.

Each module below corresponds to a single, logical data provider service defined in
the [DeFi Pulse Data documentation](https://docs.defipulse.com/).

```python
from defipulsedata import RekTo, EthGasStation, DefiPulse, DexAg, PoolsFyi

key='REPLACE-WITH-YOUR-KEY'

# Example requests for each client.

# Rek.to
rekto = RekTo(api_key=key)
rekto.get_events()

# DeFi Pulse
dp = DefiPulse(api_key=key)
dp.get_projects()

# ETH Gas Station
egs = EthGasStation(api_key=key)
egs.get_gas_price()

# DEX.AG
dexag = DexAg(api_key=key)
dexag.get_markets()

# Pools.Fyi
pools = PoolsFyi(api_key=key)
pools.get_exchanges()
```

# Contributing and Filing Issues

Contributions are welcome and encouraged.

If you have a bug or issue, please file a GitHub issue on the project describing the expected behavior and the actual behavior, with steps to reproduce the issue.

If you have a feature request, please file a GitHub issue on the project describing the feature you want, and why you want it.
