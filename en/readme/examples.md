# Examples

#### TPC-H Query 1

```
@("lineitem.csv") >> #(data: auto)
  => filter { data["l_shipdate"] <= Date("1998-12-01") - Day(90) }
  => map { l_returnflag = data["l_returnflag"]
           l_linestatus = data["l_linestatus"],
           sum_qty = data["l_quantity"].sum(),
           sum_base_price = data["l_extendedprice"].sum(),
           sum_disc_price = (data["l_extendedprice"] * (1 - data["l_discount"])).sum(),
           sum_charge = (data["l_extendedprice"] * (1 - data["l_discount"]) * (1 + data["l_tax"])).sum(),
           avg_qty = data["l_quantity"].avg(),
           avg_price = data["l_extendedprice"].avg(),
           avg_disc = data["l_discount"].avg(),
           count_order = data.count()
  }
  => group by { data["l_returnflag"], data[""l_linestatus""] }
  => sort ascend { data["l_returnflag", "l_linestatus"] }
  => slice { 0, 100 }
```
