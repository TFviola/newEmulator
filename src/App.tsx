import React, { useState, useEffect } from 'react';
import { Globe, Home, FileText, Link, Users, LogOut, HelpCircle, AlertCircle, ChevronLeft, ChevronRight, ZoomIn, ZoomOut, Printer, Sun, ToggleLeft, ToggleRight } from 'lucide-react';
import claimForm from './images/ClaimFormImage.jpg';
import claimNegativeForm from './images/ClaimNegativeImage.png';
import { jsPDF } from 'jspdf';
import myLogo from './images/myCompanyLogo.png'; 
import logo from './images/logo.png';
import SessionManager from './session/SessionManager';

function App() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [showDocumentViewer, setShowDocumentViewer] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (username && password) {
      setIsLoggedIn(true);
    }
  };

  if (showDocumentViewer) {
    return <DocumentViewer onBack={() => setShowDocumentViewer(false)} />;
  }

  if (isLoggedIn) {
    return <Dashboard onImageRequestClick={() => setShowDocumentViewer(true)} />;
  }

  return (
    <div className="bg-gray-100 min-h-screen flex items-center justify-center">
      {/* Outer background is gray. The rest is in the white 'login-wrapper'. */}

      {/* LOGIN WRAPPER (White container + orange bar + footer disclaimers) */}
      <div className="login-wrapper w-4/5 max-w-[900px] bg-white shadow-md">

        {/* ORANGE TOP BAR (inside the container, not full screen) */}
        <div className="top-bar h-[50px] w-full bg-orange-500" />

        {/* MAIN LOGIN CONTAINER: Two Columns */}
        <div className="login-container flex w-full">
          {/* LEFT COLUMN - Form */}
          <div className="login-left flex-1 p-8 min-w-[280px]">
            <h2 className="text-xl font-semibold mb-4">Welcome to QuickClaim!</h2>
            
            <form onSubmit={handleSubmit} className="flex flex-col">
              <label htmlFor="username" className="font-semibold mb-1">
                Username
              </label>
              <input
                type="text"
                id="username"
                className="border border-gray-300 rounded px-3 py-2 mb-4 w-[80%] max-w-[280px]"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
              />

              <label htmlFor="password" className="font-semibold mb-1">
                Password
              </label>
              <input
                type="password"
                id="password"
                className="border border-gray-300 rounded px-3 py-2 mb-4 w-[80%] max-w-[280px]"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />

              <button
                type="submit"
                className="btn-login w-[140px] py-2 bg-gray-300 text-white rounded hover:bg-gray-400"
              >
                Sign In
              </button>

              <div className="forgot-password mt-3">
                <a href="#" className="text-blue-600 text-sm hover:underline">
                  Forgot your password?
                </a>
              </div>
            </form>
          </div>

          {/* RIGHT COLUMN - Blue Panel */}
          <div className="login-right flex-1 flex min-w-[280px] h-auto">
            <img
            src={logo}            // or "/images/logo.png" if in public folder
            alt="Company Logo"
            className="w-full h-full object-cover"
            />
          </div>
        </div>

        {/* FOOTER (Disclaimers) - still inside .login-wrapper */}
        <footer className="text-[9px] text-center">
          <p>
            By logging into QuickClaim, you are agreeing to comply with the policies
            and restrictions outlined in the links below:
          </p>
          <p>
            <a href="#" className="text-blue-600 hover:underline">QuickClaim End User Agreement</a> |
            <a href="#" className="text-blue-600 hover:underline"> QuickClaim Privacy Notice</a>
          </p>
          <p className="mt-4">
            Copyright © 2002–2025
            Smart Data Solutions, Inc. All rights reserved.<br />
            HTTPS Connection: TLS_AES_256_GCM_SHA384
          </p>
          <p className="mt-2">
            CPT © 2025 American Medical Association. All rights reserved.<br />
            Fee schedules, relative value units, conversion factors and/or related
            components are not assigned by the AMA, are not part of CPT, and the AMA
            is not recommending their use. The AMA does not directly or indirectly practice
            medicine or dispense medical services. The AMA assumes no liability for data
            contained or not contained herein.
          </p>
          <p className="mt-4">
            CPT is a registered trademark of the American Medical Association
          </p>
          <p className="mt-2">
            U.S. Government Rights<br />
            This product includes CPT and/or CPT® Changes which are commercial
            technical data. Work was developed exclusively at private expense by the
            American Medical Association, 330 North Wabash Avenue, Chicago, Illinois
            60611. The American Medical Association does not accept licenses to
            license CPT® to the Federal Government based on the license in FAR
            12.211-7013 (Data Rights - General) and DFARS 252.227-7015 (Technical Data
            - Commercial Items) or any other license provision. The American Medical
            Association reserves all rights to approve any license with any Federal
            agency.
          </p>
        </footer>
      </div>
    </div>
  );
}

function DocumentViewer({ onBack }: { onBack: () => void }) {
  const [currentPage, setCurrentPage] = useState(1);
  const [isNegativeForm, setIsNegativeForm] = useState(false);
  const [isLoading, setIsLoading] = useState(true);
  const totalPages = 1;
  const sessionManager = SessionManager.getInstance();

  // Initialize state from session on component mount
  useEffect(() => {
    const initializeState = async () => {
      setIsLoading(true);
      // Wait for the server state to be fetched
      await new Promise(resolve => setTimeout(resolve, 100));
      setIsNegativeForm(sessionManager.getFormState());
      setIsLoading(false);
    };
    
    initializeState();
  }, []);

  // Update session when state changes
  const handleToggleForm = () => {
    const newState = !isNegativeForm;
    setIsNegativeForm(newState);
    sessionManager.setFormState(newState);
  };

  const handlePrintToPDF = () => {
    const img = new Image();
    img.crossOrigin = 'Anonymous';
    img.src = isNegativeForm ? claimNegativeForm : claimForm;

    img.onload = () => {
      const pdf = new jsPDF({
        orientation: 'portrait',
        unit: 'mm',
        format: 'a4',
      });

      const imgWidth = img.width;
      const imgHeight = img.height;
      const pageWidth = 210; // A4 width in mm
      const pageHeight = 297; // A4 height in mm

      let width = imgWidth;
      let height = imgHeight;
      const aspectRatio = imgWidth / imgHeight;

      // Scale down if wider than pageWidth
      if (width > pageWidth) {
        width = pageWidth;
        height = width / aspectRatio;
      }
      // Scale down if taller than pageHeight
      if (height > pageHeight) {
        height = pageHeight;
        width = height * aspectRatio;
      }

      // Center image on page
      const x = (pageWidth - width) / 2;
      const y = (pageHeight - height) / 2;

      pdf.addImage(img, 'JPEG', x, y, width, height);
      pdf.save('document.pdf');
    };

    img.onerror = () => {
      console.error('Failed to load image');
      alert('Error generating PDF: Unable to load image');
    };
  };

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <div className="w-full bg-blue-600">
        
        <img src={myLogo} alt="My Company Logo" className="w-full h-auto" />
        
      </div>

      {/* Navigation */}
      <div className="bg-gray-100 border-b">
        <div className="max-w-7xl mx-auto flex items-center space-x-8 px-4">
          <NavItem icon={<Home size={18} />} text="Home" onClick={onBack} />
          <NavItem icon={<FileText size={18} />} text="Reports" />
          <NavItem icon={<Link size={18} />} text="Resources" />
          <NavItem icon={<Users size={18} />} text="Account Management" />
          <div className="ml-auto flex space-x-4">
            <NavItem icon={<LogOut size={18} />} text="Logout" />
            <NavItem icon={<HelpCircle size={18} />} text="Support" />
          </div>
        </div>
      </div>

      {/* Document Summary */}
      <div className="max-w-7xl mx-auto p-4">
        <h1 className="text-2xl font-semibold mb-4">Document Summary</h1>

        <div className="flex items-center space-x-4 mb-4">
          <select className="border rounded px-3 py-1">
            <option>Health Cost Solutions</option>
          </select>
          <input
            type="text"
            value="hcs120250211257045"
            className="border rounded px-3 py-1"
            readOnly
          />
          <button className="px-4 py-1 bg-blue-500 text-white rounded hover:bg-blue-600">
            Submit
          </button>
        </div>

        {/* Document Links */}
        <div className="flex items-center space-x-4 text-blue-600 text-sm mb-4">
          <a href="#" className="hover:underline">Document Notes</a>
          <span>|</span>
          <a href="#" className="hover:underline">Document History Tracker</a>
          <span>|</span>
          <a href="#" className="hover:underline">EDI Transactions</a>
          <span>|</span>
          <a href="#" className="hover:underline">New Search</a>
          <span>|</span>
          <a href="#" className="hover:underline">Document Merge</a>
          <span>|</span>
          <div className="flex items-center space-x-2">
            <a
              href="#"
              onClick={(e) => {
                e.preventDefault();
                handlePrintToPDF();
              }}
              className="hover:underline"
            >
              Print Document to PDF
            </a>
            <button
              onClick={handleToggleForm}
              className="flex items-center space-x-1 text-gray-600 hover:text-gray-800"
              title={isNegativeForm ? "Switch to Positive Form" : "Switch to Negative Form"}
              disabled={isLoading}
            >
              {isNegativeForm ? <ToggleRight size={16} /> : <ToggleLeft size={16} />}
              <span className="text-xs">{isNegativeForm ? "Negative" : "Positive"}</span>
            </button>
          </div>
        </div>

        {/* Document Viewer Toolbar */}
        <div className="bg-gray-100 p-2 rounded-t border flex items-center space-x-4">
          <div className="flex items-center space-x-2">
            <button className="p-1 hover:bg-gray-200 rounded">
              <ChevronLeft size={20} />
            </button>
            <select className="border rounded px-2 py-1">
              <option>1</option>
            </select>
            <span>of {totalPages}</span>
            <button className="p-1 hover:bg-gray-200 rounded">
              <ChevronRight size={20} />
            </button>
          </div>

          <div className="flex items-center space-x-2">
            <input type="checkbox" id="fitImage" />
            <label htmlFor="fitImage">Fit Image</label>
          </div>

          <div className="flex items-center space-x-2">
            <button className="p-1 hover:bg-gray-200 rounded">
              <ZoomIn size={20} />
            </button>
            <button className="p-1 hover:bg-gray-200 rounded">
              <ZoomOut size={20} />
            </button>
            <button className="p-1 hover:bg-gray-200 rounded">
              <Printer size={20} />
            </button>
          </div>

          <div className="flex items-center space-x-2">
            <label>Overlay:</label>
            <select className="border rounded px-2 py-1">
              <option>None</option>
            </select>
          </div>

          <button className="p-1 hover:bg-gray-200 rounded">
            <Sun size={20} />
          </button>
        </div>

        {/* Document Display */}
        <div
          className="
            border
            w-full
            bg-white
            min-h-[800px]
            flex
            items-center
            justify-center
            overflow-auto
          "
        >
          <img
            src={isNegativeForm ? claimNegativeForm : claimForm}
            alt="Health Insurance Claim Form"
            className="w-full h-full object-contain"
          />
        </div>
      </div>
    </div>
  );
}

function Dashboard({ onImageRequestClick }: { onImageRequestClick: () => void }) {
  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header with Logo */}
      <div className="w-full bg-blue-600">
        
        <img src={myLogo} alt="My Company Logo" className="w-full h-auto" />
      
    </div>


      {/* Navigation Bar */}
      <div className="bg-gray-100 border-b">
        <div className="max-w-7xl mx-auto flex items-center space-x-8 px-4">
          <NavItem icon={<Home size={18} />} text="Home" active />
          <NavItem icon={<FileText size={18} />} text="Reports" />
          <NavItem icon={<Link size={18} />} text="Resources" />
          <NavItem icon={<Users size={18} />} text="Account Management" />
          <div className="ml-auto flex space-x-4">
            <NavItem icon={<LogOut size={18} />} text="Logout" />
            <NavItem icon={<HelpCircle size={18} />} text="Support" />
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div className="max-w-7xl mx-auto p-6">
        <div className="grid grid-cols-3 gap-6">
          {/* Main Content Area */}
          <div className="col-span-2 space-y-6">
            <div>
              <h1 className="text-2xl font-semibold text-gray-800">Welcome to the SDS QuickClaim Control Panel</h1>
              <div className="mt-2">
                <a href="#" className="text-blue-600 hover:text-blue-800">
                  Click here to view the latest updates to QuickClaim.
                </a>
                {' '}
                <a href="#" className="text-blue-600 hover:text-blue-800">[Subscribe]</a>
              </div>
            </div>

            {/* Health Cost Solutions Section */}
            <div className="bg-white rounded-lg shadow p-4">
              <h2 className="text-lg font-semibold text-gray-800">Health Cost Solutions - HCS</h2>
              <div className="text-sm text-gray-600 mt-1">24 Hour Turnaround Time</div>
              <div className="text-sm text-gray-600">Export Schedule: Every Hour</div>
              <div className="text-xs text-gray-500 mt-1">Last Refreshed - 4 minutes ago</div>
            </div>

            {/* Quick Links */}
            <div className="bg-white rounded-lg shadow p-4">
              <h2 className="text-lg font-semibold text-gray-800 mb-3">Quick Links:</h2>
              <div className="flex space-x-6">
                <a href="#" className="text-blue-600 hover:text-blue-800">Open Documents (2413)</a>
                <a href="#" className="text-blue-600 hover:text-blue-800" onClick={onImageRequestClick}>
                  Image Requests
                </a>
                <a href="#" className="text-blue-600 hover:text-blue-800">Batch Tracking Reports</a>
              </div>
            </div>

            {/* Alerts */}
            <div className="bg-white rounded-lg shadow p-4">
              <h2 className="text-lg font-semibold text-gray-800 mb-3">Alerts:</h2>
              <div className="bg-red-100 p-3 rounded">
                <div className="flex items-center text-red-800">
                  <AlertCircle size={18} className="mr-2" />
                  <span>Aging Files</span>
                  <span className="ml-auto">9</span>
                </div>
              </div>
            </div>

            {/* Queues */}
            <div className="bg-white rounded-lg shadow p-4">
              <h2 className="text-lg font-semibold text-gray-800 mb-3">Health Cost Solutions Queues:</h2>
              <table className="w-full">
                <thead>
                  <tr className="text-left text-gray-600">
                    <th className="py-2">Queue</th>
                    <th>Oldest</th>
                    <th>Count</th>
                  </tr>
                </thead>
                <tbody className="text-gray-700">
                  <tr className="border-t">
                    <td className="py-2">Eligibility Matching</td>
                    <td>16 hours</td>
                    <td>357</td>
                  </tr>
                  <tr className="border-t">
                    <td className="py-2">Pended Rejected Queue</td>
                    <td>15 hours</td>
                    <td>6</td>
                  </tr>
                  <tr className="border-t">
                    <td className="py-2">Provider Matching Queue</td>
                    <td>15 hours</td>
                    <td>2</td>
                  </tr>
                  <tr className="border-t">
                    <td className="py-2">Manual PPO Routing Queue</td>
                    <td>-</td>
                    <td>0</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

          {/* Right Sidebar */}
          <div className="space-y-6">
            <div className="bg-white rounded-lg shadow p-4">
              <h2 className="text-lg font-semibold text-gray-800 mb-3">Upcoming Maintenance Windows</h2>
              <div className="space-y-4">
                <div>
                  <div className="font-medium">Saturday Mar 15, 2025</div>
                  <div className="text-sm text-gray-600">8 PM to 4 AM CST</div>
                </div>
                <div>
                  <div className="font-medium">Saturday Apr 19, 2025</div>
                  <div className="text-sm text-gray-600">8 PM to 4 AM CST</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

function NavItem({ 
  icon, 
  text, 
  active = false,
  onClick
}: { 
  icon: React.ReactNode; 
  text: string; 
  active?: boolean;
  onClick?: () => void;
}) {
  return (
    <a
      href="#"
      onClick={(e) => {
        e.preventDefault();
        onClick?.();
      }}
      className={`flex items-center space-x-2 py-3 px-2 border-b-2 ${
        active ? 'border-blue-500 text-blue-600' : 'border-transparent text-gray-600 hover:text-blue-600'
      }`}
    >
      {icon}
      <span>{text}</span>
    </a>
  );
}

export default App;