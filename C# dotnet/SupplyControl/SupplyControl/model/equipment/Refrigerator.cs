using SupplyControl.interfaces;
using System;
using System.Collections.Generic;



namespace SupplyControl.model.equipment
{
    public class Refrigerator
    {
        private List<ISupply> supplies;
        public int id { get; private set; }

        public Type RefrigeratorType { get; private set; }

        public Refrigerator(Type type, int id)
        {
            this.id = id;
            this.RefrigeratorType = type;

            supplies = new List<ISupply>();
        }

        public void Checkin(ISupply supply) 
        {
            if (supply.GetType() != RefrigeratorType)
                throw new Exception("Tipo não suportado neste equipamento");

            if (GetSupplyByCode(supply.GetCode()) != null)
                throw new Exception("");

            supplies.Add(supply);
        }

        private ISupply GetSupplyByCode(string code) 
        {
            return this.supplies.Find(s => s.GetCode().Equals(code));
        }
    }
}
