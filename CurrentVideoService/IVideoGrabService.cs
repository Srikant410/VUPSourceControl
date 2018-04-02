using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.ServiceModel.Web;
using System.Text;

namespace CurrentVideoService
{
    // NOTE: You can use the "Rename" command on the "Refactor" menu to change the interface name "IService1" in both code and config file together.
    [ServiceContract]
    public interface IVideoGrabService
    {
        [OperationContract]
        void InsertImage(int RADDeviceID, string imageName, string imagePath);
        [OperationContract]
        Image GetImageById(int RADDeviceID);
    }
}
