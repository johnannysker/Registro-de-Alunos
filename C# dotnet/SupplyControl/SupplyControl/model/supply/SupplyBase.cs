
namespace SupplyControl.model.supply
{
    public abstract class SupplyBase
    {
        protected string code;

        public SupplyBase(string code) 
        {
            this.code = code;
        }
    }
}
