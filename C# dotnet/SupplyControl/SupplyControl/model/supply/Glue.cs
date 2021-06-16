using SupplyControl.interfaces;
using System;
using System.Collections.Generic;
using System.Text;

namespace SupplyControl.model.supply
{
    public class Glue : SupplyBase, ISupply
    {
        public Glue(string code) : base(code)
        {

        }

        public string GetCode()
        {
            return base.code;
        }
    }
}
